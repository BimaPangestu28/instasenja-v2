from rest_framework import generics
from app import serializers
from app.utils.instagram import Instagram
from app.utils.scraping import Scraping
from rest_framework.response import Response
from .models import Bot, FakeComment, History, Contact, Account

class ActionLikeCommentPostView(generics.CreateAPIView):
    serializer_class = serializers.PayloadActionLikeCommentPostSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instagram = Instagram(serializer.data)
        instagram.like_comment_post()

        return Response(data={}, status=200)

class ActionUnfollowView(generics.CreateAPIView):
    serializer_class = serializers.PayloadActionUnfollowSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instagram = Instagram(serializer.data)
        instagram.unfollow()

        return Response(data={}, status=200)

class BotListCreateView(generics.ListCreateAPIView):
    """API untuk menampilkan dan membuat Account Bot / Fake Account"""
    queryset = Bot.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.BotSerializer
        elif self.request.method == "POST":
            return serializers.PayloadBotSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            bot = Bot.objects.create(**serializer.data)

            return Response(data=serializers.BotSerializer(bot, many=False).data, status=200)
        except Exception as identifier:
            return Response(data={"message": str(identifier)}, status=400)

class BotRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """API untuk mengambil data, update dan menghapus Fake Comment"""
    queryset = Bot.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.BotSerializer
        elif self.request.method == "PUT":
            return serializers.PayloadBotSerializer

    def put(self, request, pk):
        bot = Bot.objects.filter(pk=pk)

        if bot.count() > 0:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            bot.update(**serializer.data)

            return Response(data=serializers.BotSerializer(bot.first(), many=False).data, status=200)
        else:
            return Response(data={"message": "Bot not found"}, status=404)

class FakeCommentListCreateView(generics.ListCreateAPIView):
    """API untuk menampilkan dan membuat Account Fake Comment """
    queryset = FakeComment.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.FakeCommentSerializer
        elif self.request.method == "POST":
            return serializers.PayloadFakeCommentSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            fake_comment = FakeComment.objects.create(**serializer.data)

            return Response(data=serializers.FakeCommentSerializer(fake_comment, many=False).data, status=200)
        except Exception as identifier:
            return Response(data={"message": str(identifier)}, status=400)

class FakeCommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """API untuk mengambil data, update dan menghapus Fake Comment"""
    queryset = FakeComment.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.FakeCommentSerializer
        elif self.request.method == "PUT":
            return serializers.PayloadFakeCommentSerializer

    def put(self, request, pk):
        fake_comment = FakeComment.objects.filter(pk=pk)

        if fake_comment.count() > 0:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            fake_comment.update(**serializer.data)

            return Response(data=serializers.FakeCommentSerializer(fake_comment.first(), many=False).data, status=200)
        else:
            return Response(data={"message": "Fake comment not found"}, status=404)

class ListHistoryView(generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = serializers.HistorySerializer

    ordering_fields = ["id"]

class ListContactView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = serializers.ContactSerializer

    ordering_fields = ["id"]

class ActionScrapingDataView(generics.CreateAPIView):
    serializer_class = serializers.PayloadScrapeSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        scraping = Scraping(serializer.data)
        scraping.scrape_data(serializer.data["keyword"])

        return Response(data={}, status=200)

class ActionFollowFromCompetitorView(generics.CreateAPIView):
    serializer_class = serializers.PayloadActionGetDataFromCompetitorSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instagram = Instagram(serializer.data)
        instagram.follow_from_competitor(serializer.data["username_competitor"], serializer.data["total_follow"])

        return Response(data={}, status=200)

class ActionMultiplePostView(generics.CreateAPIView):
    serializer_class = serializers.PayloadActionMultiplePostSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instagram = Instagram(serializer.data, mobile=True)
        instagram.multiple_post(serializer.data["title"], serializer.data["description"], serializer.data["image"], serializer.data["accounts"])

        return Response(data={}, status=200)

class ActionFollowFromPostView(generics.CreateAPIView):
    serializer_class = serializers.PayloadActionFollowFromPostSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instagram = Instagram(serializer.data)
        instagram.follow_from_post(serializer.data["url"])

        return Response(data={}, status=200)

class AccountListCreateView(generics.ListCreateAPIView):
    """API untuk menampilkan dan membuat Account """
    queryset = Account.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.AccountSerializer
        elif self.request.method == "POST":
            return serializers.PayloadAccountSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            account = Account.objects.create(**serializer.data)

            return Response(data=serializers.AccountSerializer(account, many=False).data, status=200)
        except Exception as identifier:
            return Response(data={"message": str(identifier)}, status=400)

class AccountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """API untuk mengambil data, update dan menghapus Account"""
    queryset = Account.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.AccountSerializer
        elif self.request.method == "PUT":
            return serializers.PayloadAccountSerializer

    def put(self, request, pk):
        account = Account.objects.filter(pk=pk)

        if account.count() > 0:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            account.update(**serializer.data)

            return Response(data=serializers.AccountSerializer(account.first(), many=False).data, status=200)
        else:
            return Response(data={"message": "Account not found"}, status=404)