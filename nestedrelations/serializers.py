from rest_framework import serializers

from .models import Parent, ChildA, ChildB, ChildA1, ChildA2


class ChildA1Serializer(serializers.ModelSerializer):

    class Meta:
        model = ChildA1
        fields = ['name']

class ChildA2Serializer(serializers.ModelSerializer):

    class Meta:
        model = ChildA2
        fields = ['name']


class ChildASerializer(serializers.ModelSerializer):
    childA1s = ChildA1Serializer(many=True, required=False)
    # childA1s = serializers.PrimaryKeyRelatedField()
    childA2s = ChildA1Serializer(many=True, required=False)

    class Meta:
        model = ChildA
        fields = ['name', 'childA1s', 'childA2s']


class ChildBSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChildB
        fields = ['name']


class ParentSerializer(serializers.ModelSerializer):

    childAs = ChildASerializer(many=True)
    childBs = ChildBSerializer(many=True)

    class Meta:
        model = Parent
        fields = ['url', 'id', 'name', 'childAs', 'childBs']
        # fields = '__all__'

    def create(self, validated_data):
        childAs_data = validated_data.pop('childAs')
        childBs_data = validated_data.pop('childBs')

        parent = Parent.objects.create(**validated_data)

        for childA_data in childAs_data:
            childA1s_data = childA_data.pop('childA1s', [])
            childA2s_data = childA_data.pop('childA2s', [])

            childA = ChildA.objects.create(parent=parent, **childA_data)

            for childA1_data in childA1s_data:
                ChildA1.objects.create(parent=childA, **childA1_data)

            for childA2_data in childA2s_data:
                ChildA2.objects.create(parent=childA, **childA2_data)

        childBInstances = []
        for childB_data in childBs_data:
            childBInstances.append(ChildB(parent=parent, **childB_data))
            # ChildB.objects.create(parent=parent, **childB_data)

        ChildB.objects.bulk_create(childBInstances)

        return parent
