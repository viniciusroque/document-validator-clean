from dataclasses import FrozenInstanceError, is_dataclass
import unittest
import uuid
from __seedwork.domain.exceptions import InvalidUuidException

from __seedwork.domain.value_objects import UniqueEntityId

class TestValueObjectUnit(unittest.TestCase):
    ...

class TestUniqueEntityIdUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = UniqueEntityId()
            value_object.id = 'fake_id'

    def test_throw_exception_when_uuid_is_invalid(self):
        with self.assertRaises(InvalidUuidException) as assert_error:
            UniqueEntityId('fake_id')

        self.assertEqual(assert_error.exception.args[0], 'ID must be a UUID valid.')

    def test_accept_uuid_passed_id_in_constructor(self):
        id_values = [uuid.uuid4(), str(uuid.uuid4()), '7bb7880f-c224-4951-8e16-68477854b171']
        for id_value in id_values:
            value_object = UniqueEntityId(id_value)
            self.assertEqual(value_object.id, str(id_value))
