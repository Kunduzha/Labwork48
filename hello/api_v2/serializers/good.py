from rest_framework import serializers

from webapp.models import Good, GoodInCart, OrderGood, Order


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ('id', 'name', 'description', 'category', 'remainder', 'price')
        read_only_fields = ('id',)


class OrderGoodSerializerForPost(serializers.ModelSerializer):

    class Meta:
        model = OrderGood
        fields = ('id', 'order', 'good', 'count')
        read_only_fields = ('id', 'order')


class OrderGoodSerializerForGet(serializers.ModelSerializer):
    good = GoodSerializer()

    class Meta:
        model = OrderGood
        fields = ('id', 'order', 'good', 'count')
        read_only_fields = ('id', 'order')



class OrderSerializerForGET(serializers.ModelSerializer):
    order_good = OrderGoodSerializerForGet(many=True)

    class Meta:
        model = Order
        fields = ('user', 'name', 'phonenumber', 'adress', 'created_at', 'updated_at', 'order_good')



class OrderSerializerForPOST(serializers.ModelSerializer):
    order_good = OrderGoodSerializerForPost(many=True)

    class Meta:
        model = Order
        fields = ('user', 'name', 'phonenumber', 'adress', 'created_at', 'updated_at', 'order_good')

    def create(self, validated_data):
        print(validated_data)
        order = Order.objects.create(user=validated_data['user'], name=validated_data['name'],
                                     adress=validated_data['adress'], phonenumber=validated_data['phonenumber'])
        for goods in validated_data['order_good']:
            good_in_order = OrderGood.objects.create(order=order, good=goods['good'], count=goods['count'])
            print(good_in_order)
        return validated_data

