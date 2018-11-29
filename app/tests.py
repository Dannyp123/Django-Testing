from django.test import SimpleTestCase
from django.urls import reverse


class TestAddCanHandleSimpleAddition(SimpleTestCase):
    '''
    0+0 = 0
    2+2=4
    2.3 + 1.2 = 3.5
    2+-1 = 1
    -2+-3 = -5

    '''

    def test_two_plus_two(self):
        response = self.client.get(
            path=reverse('add'),
            data={
                "num1": '2',
                "num2": '2'
            },
        )

        self.assertEqual(response.context['answer'], 4)

    def test_two_plus_negative_one(self):
        response = self.client.get(
            path=reverse('add'),
            data={
                "num1": '2',
                "num2": '-1'
            },
        )
        self.assertEqual(response.context["answer"], 1)

    def test_zero_plus_zero(self):
        response = self.client.get(
            path=reverse('add'),
            data={
                "num1": '0',
                "num2": '0'
            },
        )

        self.assertEqual(response.context["answer"], 0)

    def test_float_plus_float(self):
        response = self.client.get(
            path=reverse('add'),
            data={
                "num1": '2.3',
                "num2": '1.2'
            },
        )

        self.assertEqual(response.context["answer"], 3.5)

    def test_neg_plus_neg(self):
        response = self.client.get(
            path=reverse('add'),
            data={
                "num1": '-2',
                "num2": '-3'
            },
        )

        self.assertEqual(response.context["answer"], -5)


class TestAddWithoutNumbers(SimpleTestCase):
    ''' If add is not given two numbers it should present the user with the add.html template and not try to compute and answer'''

    def test_given_non_numeric_input(self):
        response = self.client.get(
            path=reverse('add'),
            data={
                "num1": 'a',
                "num2": 'b'
            },
        )

        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn("answer", response.context)

    def test_given_one_empty_inputs(self):
        response = self.client.get(
            path=reverse('add'),
            data={
                "num1": " ",
                "num2": "1"
            },
        )

        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn("answer", response.context)

    def test_given_two_empty_inputs(self):
        response = self.client.get(
            path=reverse('add'),
            data={
                "num1": " ",
                "num2": " "
            },
        )
        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn("answer", response.context)

    def test_given_two_list(self):
        response = self.client.get(
            path=reverse('add'),
            data={
                "num1": "[1,2,3,4]",
                "num2": "[5,6,7,8]"
            },
        )
        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)


class TestAddCanHandleSimpleDoubling(SimpleTestCase):
    ''' 
    4*2=8
    8*2=16
    0*0=0
    0*2=0
    1*2=2
    2.2*2=4.4
    -4*2=-8
    '''

    def test_four_doubled(self):
        response = self.client.get(
            path=reverse('double'),
            data={"num1": '4'},
        )

        self.assertEqual(response.context["solution"], 8)
