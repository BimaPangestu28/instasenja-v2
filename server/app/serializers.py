from rest_framework import serializers
from .models import Bot, FakeComment, History, Contact, Account

class PayloadActionLikeCommentPostSerializer(serializers.Serializer):
    total_comment = serializers.IntegerField()
    total_like = serializers.IntegerField()
    comment_category = serializers.CharField()
    url = serializers.CharField()
    random_code = serializers.CharField()

class PayloadActionUnfollowSerializer(serializers.Serializer):
    account_id = serializers.CharField()
    total_unfollow = serializers.IntegerField()
    random_code = serializers.CharField()

class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ("__all__")

class PayloadBotSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "username",)

class PayloadAccountSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class FakeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeComment
        fields = ("__all__")

class PayloadFakeCommentSerializer(serializers.Serializer):
    comment = serializers.CharField()
    category = serializers.CharField()

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ("__all__")

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("__all__")

class PayloadScrapeSerializer(serializers.Serializer):
    keyword = serializers.CharField()
    random_code = serializers.CharField()

class PayloadActionGetDataFromCompetitorSerializer(serializers.Serializer):
    account_id = serializers.CharField()
    username_competitor = serializers.CharField()
    total_follow = serializers.IntegerField()
    random_code = serializers.CharField()

class PayloadActionMultiplePostSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    description = serializers.CharField()
    accounts = serializers.ListField()
    random_code = serializers.CharField()

class PayloadActionFollowFromPostSerializer(serializers.Serializer):
    url = serializers.CharField()
    account_id = serializers.CharField()
    random_code = serializers.CharField()

class ActionLikeByTagSerializer(serializers.Serializer):
    account_id = serializers.CharField()
    total_like = serializers.IntegerField()
    tag = serializers.CharField()