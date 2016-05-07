from rest_framework import serializers
from gymmy_app.models import TrainingPlanExerciseDetail
from gymmy_app.serializers.exercise_serializer import ExerciseSerializer
from gymmy_app.serializers.training_plan_exercise_progress_serializer import TrainingPlanExerciseProgressSerializer


class TrainingPlanExerciseDetailSerializer(serializers.ModelSerializer):
    exercise_instance = ExerciseSerializer(source='exercise', read_only=True)
    lastest_exercise_progress = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TrainingPlanExerciseDetail
        fields = ('id', 'training_plan', 'exercise', 'lastest_exercise_progress', 'exercise_instance', 'breaks_between_exercises', 'trainer_notes', 'trainee_notes')
        extra_kwargs = {'exercise': {'write_only': True}}

    def get_lastest_exercise_progress(self, obj):
        lastest_exercise_progress = obj.exercise_progress.all()
        print lastest_exercise_progress
        if len(lastest_exercise_progress) is not 0:
            return TrainingPlanExerciseProgressSerializer(lastest_exercise_progress.latest('date')).data
        else:
            return None
