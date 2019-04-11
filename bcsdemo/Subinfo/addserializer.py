from rest_framework import serializers

from .models import contcatagory,contentelement,contentelementimage,contenttabletitle,contenttableinfo,types,question




class Questionserializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model=question
        fields=[

            'id',
            'title',
            'que_pic',
            'op1',
            'op2',
            'op3',
            'op4',
            'ans',
            'explain'
        ]



class QuestionTypeserializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    allquestion=Questionserializer(many=True)
    class Meta:
        model=types
        fields=[
            'id',
            'title',
            'allquestion'

        ]

class ContenttableInfoserializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model=contenttableinfo
        fields=[
            'id',
            'tl1',
            'tl2',
            'tl3',
            'tl4',
            'tl5',
            'tl6',

        ]
class Contettabletitle(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    tableinfo=ContenttableInfoserializer(many=True)
    class Meta:
        model=contenttabletitle
        fields=[
            'id',
            'title',
            'cl1',
            'cl2',
            'cl3',
            'cl4',
            'cl5',
            'cl6',
            'tableinfo'

        ]
class Contentimage(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)

    class Meta:
        model=contentelementimage
        fields=[
            'id',
            'content_pic',
            'title'

        ]


class Contentelemteserializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    images=Contentimage(many=True)
    contenttable=Contettabletitle(many=True)
    #qutypes=QuestionTypeserializer(many=True)
    class Meta:
        model=contentelement
        fields=[
            'id',
            'title',
            'content',
            'images',
            'contenttable',
            #'qutypes'
        ]



class Contcataserializer(serializers.ModelSerializer):
    contents = Contentelemteserializer(many=True)
    class Meta:
        model=contcatagory
        fields = [
            'id',
            'contentlist',
            'cata_pic',
            'contents'
        ]

