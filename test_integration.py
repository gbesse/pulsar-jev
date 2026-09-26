import json
import unittest
from pulsar_jev import JevDecisionFunction

class FunctionTest(unittest.TestCase):
    def test_envelope(self):
        fn = JevDecisionFunction()
        class Client:
            def decide(self, text):
                assert text == 'works'
                return {'route':'yes','probability':0.9,'state_sha256':'abc'}
        fn.client = Client()
        class Context:
            def get_user_config_value(self, key):
                return 'text' if key == 'text_field' else None
        output = json.loads(fn.process(json.dumps({'text':'works'}), Context()))
        self.assertEqual('yes', output['jev']['route'])
