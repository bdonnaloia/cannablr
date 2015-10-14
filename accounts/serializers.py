from accounts.models import Entry
from rest_framework import serializers

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('headline', 'body_text', 'author', 'pub_date', 'zipcode', 'price1', 'price2', 'price3', 'price4', 'price5', 'entrytype', 'item_picture')