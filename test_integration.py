import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile
from pulsar_jev import JevDecisionFunction
from package import build

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

    def test_package_has_importable_modules(self):
        with tempfile.TemporaryDirectory() as directory:
            archive = build(Path(directory) / 'function.zip')
            with ZipFile(archive) as package:
                self.assertIn('src/pulsar_jev.py', package.namelist())
                self.assertIn('src/jev_common.py', package.namelist())
            env = dict(os.environ, PYTHONPATH=str(archive) + '/src')
            check = subprocess.run([sys.executable,'-c',
                'import pulsar_jev, jev_common; assert hasattr(pulsar_jev, "JevDecisionFunction")'],
                cwd=directory, env=env, capture_output=True, text=True)
            self.assertEqual(0, check.returncode, check.stderr)
