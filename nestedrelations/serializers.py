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
    childA1s = ChildA1Serializer(many=True, read_only=True)
    childA2s = ChildA1Serializer(many=True, read_only=True)

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
            ChildA.objects.create(parent=parent, **childA_data)

        for childB_data in childBs_data:
            ChildB.objects.create(parent=parent, **childB_data)

        return parent
