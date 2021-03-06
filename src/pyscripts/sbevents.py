events = {}
policy_events = {}

def registerPolicyEventHandler(event, handler):
	if not policy_events.has_key(event):
		policy_events[event] = []
	policy_events[event].append(handler)

def registerEventHandler(event, handler):
	if not events.has_key(event):
		events[event] = []
	events[event].append(handler)

def triggerEvent(event, args):
	if events.has_key(event):
		for handler in events[event]:
			handler(*args)

def triggerPolicyEvent(event, args):
	if policy_events.has_key(event):
		for handler in policy_events[event]:
			if not handler(*args):
				return False
	return True
