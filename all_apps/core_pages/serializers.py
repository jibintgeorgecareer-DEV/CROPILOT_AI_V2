from rest_framework import serializers
from .models import Feedback

class FeedbackAPI_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ['feedback_text','created_at']

    def create(self, validated_data):
        request = self.context['request']

        feedback = Feedback.objects.create(user=request.user, feedback_text=validated_data['feedback_text'])

        return feedback
