from django.urls import path
from app import views

app_name = "app"

urlpatterns = [
    path("actions/like-comment-post", views.ActionLikeCommentPostView.as_view()),
    path("actions/unfollow", views.ActionUnfollowView.as_view()),
    path("actions/scraping-data", views.ActionScrapingDataView.as_view()),
    path("actions/follow-from-competitor", views.ActionFollowFromCompetitorView.as_view()),
    path("actions/multiple-post", views.ActionMultiplePostView.as_view()),
    path("actions/follow-from-post", views.ActionFollowFromPostView.as_view()),

    path("bots", views.BotListCreateView.as_view()),
    path("bots/<int:pk>", views.BotRetrieveUpdateDestroyView.as_view()),

    path("fake-comments", views.FakeCommentListCreateView.as_view()),
    path("fake-comments/<int:pk>", views.FakeCommentRetrieveUpdateDestroyView.as_view()),

    path("histories", views.ListHistoryView.as_view()),
    path("contacts", views.ListContactView.as_view()),
]