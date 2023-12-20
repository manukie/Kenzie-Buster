from .serializers import UserSerializer, LoginSerializer
from .models import User
from rest_framework.views import APIView, status, Request, Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner, IsEmployee
from django.shortcuts import get_object_or_404


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(date=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_date["password"]
        )

        if not user:
            return Response({"detail": "No active account found with the given credentials"},
                            status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)

        token_data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

        return Response(token_data)


class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner | IsEmployee]

    def get(self, request: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, pk=user_id)
        serializer = UserSerializer(found_user)
        self.check_object_permissions(request, found_user)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, pk=user_id)
        serializer = UserSerializer(found_user, data=request.data, partial=True)
        self.check_object_permissions(request, found_user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
