from dataclasses import FrozenInstanceError, is_dataclass
from datetime import datetime
import unittest
from document.domain.entities import Document


class TestDocumentUnit(unittest.TestCase):

    def test_if_is_dataclass(self):
        self.assertTrue(is_dataclass(Document))

    def test_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            document = Document(document='70319119823')
            document.document = 'fakedocument'

    def test_constructor(self):
        document1 = Document(
            document='70319119823',
            created_at=datetime.utcnow()
        )

        self.assertEqual(document1.document, '70319119823')
        self.assertIsInstance(document1.created_at, datetime)

    def test_if_id_is_generated_in_contructor(self):
        document1 = Document(document='70319119823')
        document2 = Document(document='70319119823')
        self.assertNotEqual(document1.id, document2.id)

    def test_if_created_at_is_generated_in_contructor(self):
        document1 = Document(document='70319119823')
        document2 = Document(document='70319119823')
        self.assertNotEqual(document1.created_at, document2.created_at)

    def test_created_at(self):
        created_at = datetime.utcnow()
        document1 = Document(document='70319119823', created_at=created_at)
        self.assertEqual(created_at, document1.created_at)
