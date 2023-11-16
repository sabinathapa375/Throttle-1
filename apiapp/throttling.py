from rest_framework.throttling import UserRateThrottle

class SabinaRateThrottle(UserRateThrottle):
    scope = 'sabina'
    