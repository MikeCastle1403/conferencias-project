from datetime import time

speakers = [
    {
        "id": 1,
        "first_name": "Alice",
        "last_name": "Johnson",
        "role": "Arquitecta Cloud",
        "company": "TechStream",
        "linkedin": "https://www.linkedin.com/in/dummy-alice",
        "image": "https://i.pravatar.cc/150?u=alice"
    },
    {
        "id": 2,
        "first_name": "Bob",
        "last_name": "Smith",
        "role": "Ingeniero de Datos",
        "company": "DataFlow Systems",
        "linkedin": "https://www.linkedin.com/in/dummy-bob",
        "image": "https://i.pravatar.cc/150?u=bob"
    },
    {
        "id": 3,
        "first_name": "Charlie",
        "last_name": "Davis",
        "role": "Especialista DevOps",
        "company": "OpsWorks",
        "linkedin": "https://www.linkedin.com/in/dummy-charlie",
        "image": "https://i.pravatar.cc/150?u=charlie"
    },
    {
        "id": 4,
        "first_name": "Diana",
        "last_name": "Evans",
        "role": "Investigadora ML",
        "company": "AI Dynamics",
        "linkedin": "https://www.linkedin.com/in/dummy-diana",
        "image": "https://i.pravatar.cc/150?u=diana"
    },
    {
        "id": 5,
        "first_name": "Evan",
        "last_name": "Wright",
        "role": "Consultor de Seguridad",
        "company": "SecureNet",
        "linkedin": "https://www.linkedin.com/in/dummy-evan",
        "image": "https://i.pravatar.cc/150?u=evan"
    },
    {
        "id": 6,
        "first_name": "Fiona",
        "last_name": "Green",
        "role": "Gerente de Producto",
        "company": "CloudNative",
        "linkedin": "https://www.linkedin.com/in/dummy-fiona",
        "image": "https://i.pravatar.cc/150?u=fiona"
    },
    {
        "id": 7,
        "first_name": "George",
        "last_name": "Hall",
        "role": "Ingeniero de Software",
        "company": "CodeCraft",
        "linkedin": "https://www.linkedin.com/in/dummy-george",
        "image": "https://i.pravatar.cc/150?u=george"
    },
    {
        "id": 8,
        "first_name": "Hannah",
        "last_name": "Lee",
        "role": "CTO",
        "company": "FutureTech",
        "linkedin": "https://www.linkedin.com/in/dummy-hannah",
        "image": "https://i.pravatar.cc/150?u=hannah"
    }
]

# Helper to find speaker by ID
def get_speakers_by_ids(ids):
    return [s for s in speakers if s["id"] in ids]

events = [
    {
        "id": 1,
        "title": "Keynote: El Futuro de la Computación en la Nube",
        "speakers": get_speakers_by_ids([8]),
        "category": "Keynote",
        "description": "Una charla de apertura inspiradora sobre las últimas tendencias en tecnología de la nube y lo que depara el futuro para Google Cloud Platform.",
        "start_time": "09:00",
        "end_time": "10:00",
        "type": "charla"
    },
    {
        "id": 2,
        "title": "Escalando con Google Kubernetes Engine",
        "speakers": get_speakers_by_ids([1, 3]),
        "category": "Infraestructura",
        "description": "Análisis profundo de las mejores prácticas de autoescalado de GKE y estrategias de gestión de múltiples clústeres para escala empresarial.",
        "start_time": "10:15",
        "end_time": "11:00",
        "type": "charla"
    },
    {
        "id": 3,
        "title": "Arquitecturas Serverless con Cloud Run",
        "speakers": get_speakers_by_ids([7]),
        "category": "Desarrollo de Apps",
        "description": "Aprenda a construir y desplegar aplicaciones en contenedores escalables en una plataforma serverless totalmente gestionada.",
        "start_time": "11:15",
        "end_time": "12:00",
        "type": "charla"
    },
    {
        "id": 4,
        "title": "Descanso para Almorzar",
        "speakers": [],
        "category": "Descanso",
        "description": "Almuerzo de networking en la cafetería. Opciones veganas y sin gluten disponibles.",
        "start_time": "12:00",
        "end_time": "13:00",
        "type": "descanso"
    },
    {
        "id": 5,
        "title": "BigQuery: Analizando Petabytes de Datos",
        "speakers": get_speakers_by_ids([2]),
        "category": "Datos y Analítica",
        "description": "Desbloquee el poder de BigQuery para análisis en tiempo real y almacenamiento de datos. Consejos sobre optimización y gestión de costos.",
        "start_time": "13:00",
        "end_time": "13:45",
        "type": "charla"
    },
    {
        "id": 6,
        "title": "IA/ML en Google Cloud: Vertex AI",
        "speakers": get_speakers_by_ids([4, 6]),
        "category": "IA y ML",
        "description": "Un vistazo completo a Vertex AI para construir, desplegar y escalar modelos de aprendizaje automático.",
        "start_time": "14:00",
        "end_time": "14:45",
        "type": "charla"
    },
    {
        "id": 7,
        "title": "Asegurando su Carga de Trabajo en la Nube",
        "speakers": get_speakers_by_ids([5]),
        "category": "Seguridad",
        "description": "Mejores prácticas para IAM, VPC Service Controls y la seguridad de la cadena de suministro de software en GCP.",
        "start_time": "15:00",
        "end_time": "15:45",
        "type": "charla"
    },
    {
        "id": 8,
        "title": "Escala Global con Cloud Spanner",
        "speakers": get_speakers_by_ids([2]),
        "category": "Datos y Analítica",
        "description": "Descubra cómo Cloud Spanner ofrece consistencia fuerte y alta disponibilidad a escala global.",
        "start_time": "16:00",
        "end_time": "16:30",
        "type": "charla"
    },
     {
        "id": 11,
        "title": "Palabras de Cierre",
        "speakers": [],
        "category": "Keynote",
        "description": "Resumen del día.",
        "start_time": "18:00",
        "end_time": "18:15",
        "type": "charla"
    }
]
