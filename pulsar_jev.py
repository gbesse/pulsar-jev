"""Pulsar Function that emits a decision envelope to its output topic."""
import json
try:
    from pulsar import Function
except ImportError:
    Function = object
from jev_common import JevClient

class JevDecisionFunction(Function):
    def __init__(self):
        self.client = None

    def process(self, input, context):
        if self.client is None:
            question = context.get_user_config_value('question')
            if not question:
                raise ValueError('question user config is required')
            threshold = float(context.get_user_config_value('threshold') or 0.8)
            self.client = JevClient(question, threshold=threshold)
        field = context.get_user_config_value('text_field') or 'text'
        event = json.loads(input.decode('utf-8') if isinstance(input, bytes) else input)
        if not isinstance(event, dict) or not isinstance(event.get(field), str):
            raise ValueError('input must be a JSON object containing the text field')
        if 'jev' in event:
            raise ValueError('jev field already exists')
        event['jev'] = self.client.decide(event[field])
        return json.dumps(event, ensure_ascii=False, separators=(',', ':'))
