from django.db import transaction
from rest_framework import serializers, exceptions

from .models import Parent, ChildA, ChildB, ChildA1, ChildA2


def delete_key(obj, key):
    try: del obj[key]
    except KeyError: pass
    return obj

class ChildA1Serializer(serializers.ModelSerializer):

    class Meta:
        model = ChildA1
        fields = ['id', 'name']
        extra_kwargs = {'id': {'read_only': False, 'required': False}}

class ChildA2Serializer(serializers.ModelSerializer):

    class Meta:
        model = ChildA2
        fields = ['id', 'name']
        extra_kwargs = {'id': {'read_only': False, 'required': False}}


class ChildASerializer(serializers.ModelSerializer):
    childA1s = ChildA1Serializer(many=True, required=False)
    # childA1s = serializers.PrimaryKeyRelatedField()
    childA2s = ChildA1Serializer(many=True, required=False)

    class Meta:
        model = ChildA
        fields = ['id', 'name', 'dt', 'childA1s', 'childA2s']
        extra_kwargs = {'id': {'read_only': False, 'required': False}}


class ChildBSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChildB
        fields = ['id', 'name']
        extra_kwargs = {'id': {'read_only': False, 'required': False}}


class ParentSerializer(serializers.ModelSerializer):

    childAs = ChildASerializer(many=True)
    childBs = ChildBSerializer(many=True)

    class Meta:
        model = Parent
        fields = ['url', 'id', 'name', 'childAs', 'childBs']
        # fields = '__all__'

    @transaction.atomic
    def create(self, validated_data):
        # raise exceptions.ValidationError({"msg": "test"})
        childAs_data = validated_data.pop('childAs')
        childBs_data = validated_data.pop('childBs')

        parent = Parent.objects.create(**validated_data)

        for childA_data in childAs_data:
            delete_key(childA_data, 'id')

            childA1s_data = childA_data.pop('childA1s', [])
            childA2s_data = childA_data.pop('childA2s', [])

            childA = ChildA.objects.create(parent=parent, **childA_data)

            for childA1_data in childA1s_data:
                delete_key(childA1_data, 'id')
                ChildA1.objects.create(parent=childA, **childA1_data)

            for childA2_data in childA2s_data:
                delete_key(childA2_data, 'id')
                ChildA2.objects.create(parent=childA, **childA2_data)

        childBInstances = []
        for childB_data in childBs_data:
            delete_key(childB_data, 'id')

            childBInstances.append(ChildB(parent=parent, **childB_data))
            # ChildB.objects.create(parent=parent, **childB_data)

        ChildB.objects.bulk_create(childBInstances)

        return parent

    def create_or_update_childA(self, childA_data, parent):
        childA_id = childA_data.pop('id', None)
        if childA_id:
            try:
                childA = ChildA.objects.get(pk=childA_id)
                for attr, val in childA_data.items():
                    setattr(childA, attr, val)
                childA.save()
                return childA
            except ChildA.DoesNotExist:
                return ChildA.objects.create(parent=parent, **childA_data)
        else:
            return ChildA.objects.create(parent=parent, **childA_data)

    def create_or_update_childB(self, childB_data, parent):
        childB_id = childB_data.pop('id', None)
        if childB_id:
            try:
                childB = ChildB.objects.get(pk=childB_id)
                for attr, val in childB_data.items():
                    setattr(childB, attr, val)
                childB.save()
            except ChildB.DoesNotExist:
                ChildB.objects.create(parent=parent, **childB_data)
        else:
            ChildB.objects.create(parent=parent, **childB_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        childAs_data = validated_data.pop('childAs', None)
        childBs_data = validated_data.pop('childBs', None)

        if (childAs_data):
            for childA_data in childAs_data:
                childA1s_data = childA_data.pop('childA1s', [])
                childA2s_data = childA_data.pop('childA2s', [])

                childA = self.create_or_update_childA(childA_data, instance)

                for childA1_data in childA1s_data:
                    childA1_id = childA1_data.pop('id', None)
                    if (childA1_id):
                        try:
                            childA1 = ChildA1.objects.get(pk=childA1_id)
                            for attr, val in childA1_data.items():
                                setattr(childA1, attr, val)
                            childA1.save()
                        except ChildA1.DoesNotExist:
                            ChildA1.objects.create(parent=childA, **childA1_data)
                    else:
                        ChildA1.objects.create(parent=childA, **childA1_data)

                for childA2_data in childA2s_data:
                    childA2_id = childA2_data.pop('id', None)
                    if (childA2_id):
                        try:
                            childA2 = ChildA2.objects.get(pk=childA2_id)
                            for attr, val in childA2_data.items():
                                setattr(childA2, attr, val)
                            childA2.save()
                        except ChildA2.DoesNotExist:
                            ChildA2.objects.create(parent=childA, **childA2_data)
                    else:
                        ChildA2.objects.create(parent=childA, **childA2_data)


        if (childBs_data):
            for childB_data in childBs_data:
                self.create_or_update_childB(childB_data, instance)

        # instance.name = validated_data.get('name', instance.name)
        for attr, val in validated_data.items():
            setattr(instance, attr, val)

        instance.save()

        # raise Exception('Make transaction fail')
        return instance
