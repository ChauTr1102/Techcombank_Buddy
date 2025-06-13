from api.services import *

def MultiAgent(user_input):
    routing_response = RoutingAgent().prompt_routing(user_input)
    if routing_response == "Navigation":
        pass
    elif routing_response == "Recommendation":
        pass
    elif routing_response == "Transaction":
        pass
    elif routing_response == "Assistant":
        pass
        