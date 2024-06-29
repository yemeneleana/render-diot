# main/management/commands/create_articles.py

from django.core.management.base import BaseCommand
from main.models import Article

class Command(BaseCommand):
    help = 'Creates initial articles on machine learning'

    def handle(self, *args, **kwargs):
        # Supprime tous les articles existants pour éviter les doublons lors de l'exécution multiple du script
        Article.objects.all().delete()

        # Création des articles sur le machine learning
        articles = [
            {
                'title': "Introduction to Machine Learning",
                'content': "Machine learning is a branch of artificial intelligence (AI) that allows machines to learn patterns from data and make decisions without human intervention...",
                'language': 'en'
            },
            {
                'title': "Supervised Learning",
                'content': "Supervised learning is a type of machine learning where the algorithm learns from labeled data...",
                'language': 'en'
            },
            {
                'title': "Unsupervised Learning",
                'content': "Unsupervised learning is a type of machine learning where the algorithm learns patterns from unlabeled data...",
                'language': 'en'
            },
            {
                'title': "Reinforcement Learning",
                'content': "Reinforcement learning is a type of machine learning where an agent learns to make decisions in an environment to achieve maximum reward...",
                'language': 'en'
            },
        ]

        # Créer chaque article dans la base de données
        for article_data in articles:
            Article.objects.create(**article_data)

        self.stdout.write(self.style.SUCCESS('Successfully created articles on machine learning'))
