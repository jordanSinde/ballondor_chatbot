from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    """Affiche la page du chatbot"""
    return render(request, "chatbot/index.html")

@csrf_exempt
def get_response(request):
    """Répond aux questions du chatbot"""
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "").lower().strip()
        
        # Base de connaissances sur le Ballon d"Or 2024
        # On vérifie d"abord les questions les plus spécifiques
        
        # Ballon d"Or féminin (vérifier EN PREMIER car plus spécifique)
        if any(keyword in user_message for keyword in ["féminin", "femme", "feminine", "gagnante"]):
            return JsonResponse({"response": "Aitana Bonmatí a remporté le Ballon d\"Or féminin 2024 ! La joueuse du FC Barcelone a été couronnée pour la deuxième année consécutive."})
        
        # Trophée Kopa
        if any(keyword in user_message for keyword in ["kopa", "jeune joueur", "meilleur jeune", "yamal"]):
            return JsonResponse({"response": "Lamine Yamal a remporté le Trophée Kopa 2024 ! Le jeune prodige du FC Barcelone (17 ans) a été désigné meilleur joueur de moins de 21 ans."})
        
        # Lieu de la cérémonie
        if any(keyword in user_message for keyword in ["où", "lieu", "endroit", "déroulée", "deroulee"]):
            return JsonResponse({"response": "La cérémonie s\"est déroulée au Théâtre du Châtelet à Paris, en France."})
        
        # Date de la cérémonie
        if any(keyword in user_message for keyword in ["date", "quand", "quel jour"]):
            return JsonResponse({"response": "La cérémonie du Ballon d\"Or 2024 a eu lieu le 28 octobre 2024."})
        
        # Ballon d"Or masculin (vérifier EN DERNIER car plus général)
        if any(keyword in user_message for keyword in ["ballon d\"or", "ballon d'or", "gagnant", "vainqueur", "remporté", "homme", "masculin", "cette année", "cette annee"]):
            return JsonResponse({"response": "Rodri a remporté le Ballon d\"Or 2024 ! Le milieu de terrain de Manchester City et de l\"équipe d\"Espagne a été récompensé pour sa saison exceptionnelle."})
        
        # Réponse par défaut
        default_response = """Je ne suis pas sûr de comprendre votre question. 
        
Je peux répondre aux questions suivantes :
- Qui a remporté le Ballon d\"Or masculin ?
- Qui a remporté le Ballon d\"Or féminin ?
- Où s\"est déroulée la cérémonie ?
- Quelle est la date de la cérémonie ?
- Qui a remporté le Trophée Kopa ?"""
        return JsonResponse({"response": default_response})
    
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)