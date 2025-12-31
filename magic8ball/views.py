from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .utils import get_magic8ball_answer


def predict(request):
    """
    Handle magic 8-ball predictions.
    GET: Display form
    POST: Return prediction based on question hash
    """
    context = {
        'title': 'Magic 8-Ball',
        'answer': None,
        'question': None,
    }

    if request.method == 'POST':
        question = request.POST.get('question', '').strip()
        if question:
            answer = get_magic8ball_answer(question)
            context['answer'] = answer
            context['question'] = question

    return render(request, 'magic8ball/predict.html', context)


@csrf_exempt
@require_http_methods(["POST"])
def api_predict(request):
    """
    API endpoint for magic 8-ball predictions.
    POST JSON: {"question": "..."}
    Returns JSON: {"question": "...", "answer": "...", "status": "ok"}
    """
    try:
        data = json.loads(request.body)
        question = data.get('question', '').strip()

        if not question:
            return JsonResponse({
                'status': 'error',
                'message': 'Question is required'
            }, status=400)

        answer = get_magic8ball_answer(question)

        return JsonResponse({
            'question': question,
            'answer': answer,
            'status': 'ok'
        })
    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid JSON'
        }, status=400)


def health(request):
    """
    Health check endpoint.
    """
    return JsonResponse({
        'status': 'ok',
        'service': 'predictor'
    })
