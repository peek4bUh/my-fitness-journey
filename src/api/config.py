from flask_restx import Api


api_restx = Api(
    title="MyFitnessJourney",
    version="0.0.1",
    doc="/api/v0/schema/ui",
    prefix="/api/v0",
    authorizations={
        'apikey': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'X-API-KEY'
        }
    },
    security='apikey'
)
