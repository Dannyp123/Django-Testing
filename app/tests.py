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
        response = self.client.post(
            path=reverse('add'),
            data={
                "num1": '2',
                "num2": '2'
            },
        )

        self.assertEqual(response.context['answer'], 4)

    def test_two_plus_negative_one(self):
        response = self.client.post(
            path=reverse('add'),
            data={
                "num1": '2',
                "num2": '-1'
            },
        )
        self.assertEqual(response.context["answer"], 1)

    def test_zero_plus_zero(self):
        response = self.client.post(
            path=reverse('add'),
            data={
                "num1": '0',
                "num2": '0'
            },
        )

        self.assertEqual(response.context["answer"], 0)

    def test_float_plus_float(self):
        response = self.client.post(
            path=reverse('add'),
            data={
                "num1": '2.3',
                "num2": '1.2'
            },
        )

        self.assertEqual(response.context["answer"], 3.5)

    def test_neg_plus_neg(self):
        response = self.client.post(
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


class TestDoubleCanHandleSimpleDoubling(SimpleTestCase):
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

    def test_eight_doubled(self):
        response = self.client.get(
            path=reverse('double'),
            data={"num1": '8'},
        )
        self.assertEqual(response.context['solution'], 16)

    def test_zero_doubled(self):
        response = self.client.get(
            path=reverse('double'),
            data={'num1': '0'},
        )
        self.assertEqual(response.context['solution'], 0)

    def test_float_doubled(self):
        response = self.client.get(
            path=reverse('double'),
            data={'num1': '2.2'},
        )
        self.assertEqual(response.context['solution'], 4.4)

    def test_negative_four_doubled(self):
        response = self.client.get(
            path=reverse('double'),
            data={'num1': '-4'},
        )
        self.assertEqual(response.context['solution'], -8)

    def test_one_doubled(self):
        response = self.client.get(
            path=reverse('double'),
            data={'num1': '1'},
        )
        self.assertEqual(response.context['solution'], 2)

class TestDoubleCanHandleNonNumber(SimpleTestCase):
    def test_given_non_numeric_input_for_double(self):
        response = self.client.get(
            path=reverse('double'),
            data={
                "num1": 'a'
            },
        )
        self.assertTemplateUsed(response, 'app/double.html')
        self.assertNotIn("answer", response.context)

    def test_given_one_empty_inputs_for_double(self):
        response = self.client.get(
            path=reverse('double'),
            data={
                "num1": " "
            },
        )
        self.assertTemplateUsed(response, 'app/double.html')
        self.assertNotIn("answer", response.context)

class TestTripleCanHandleSimpleTripling(SimpleTestCase):
    '''
    4*3=12
    10*3=30
    0*3=0
    1*3=3
    7.5 * 3=22.5
    -12 * 3 = -36 
    '''

    def test_four_tripled(self):
        response = self.client.get(
            path=reverse('triple'),
            data={"num1": '4'},
        )
        self.assertEqual(response.context['answer'], 12)

    def test_ten_tripled(self):
        response = self.client.get(
            path=reverse("triple"),
            data={"num1": '10'},
        )
        self.assertEqual(response.context['answer'], 30)

    def test_one_tripled(self):
        response = self.client.get(
            path=reverse("triple"),
            data={"num1": '1'},
        )
        self.assertEqual(response.context.get('answer'), 3)


class TestTripleCanHandleBadCases(SimpleTestCase):
    def test_given_non_numeric_input_for_triple(self):
        response = self.client.get(
            path=reverse('triple'),
            data={
                "num1": 'a',
            },
        )
        self.assertTemplateUsed(response, 'app/triple.html')
        self.assertNotIn('answer', response.context)

class TestEarnings(SimpleTestCase):
    def test_total_seats(self):
        response = self.client.get(
            path=reverse("earnings"),
            data={
                'seat_a': '4',
                'seat_b': '3',
                'seat_c': '5'
            },
        )
        self.assertEqual(response.context.get('answer'), 141)

    def test_total_seats_second(self):
        response = self.client.get(
            path=reverse("earnings"),
            data={
                'seat_a': '5',
                'seat_b': '6',
                'seat_c': '2'
            },
        )
        self.assertEqual(response.context.get("answer"), 165)

    def test_total_seats_third(self):
        response = self.client.get(
            path=reverse("earnings"),
            data={
                'seat_a': '2',
                'seat_b': '1',
                'seat_c': '4'
            },
        )
        self.assertEqual(response.context.get("answer"), 78)

class TestInvalidSeats(SimpleTestCase):
    def test_no_seats(self):
        response = self.client.get(
            path=reverse("earnings"),
            data={
                'seat_a': '',
                'seat_b': '',
                'seat_c': ''
            },
        )
        self.assertTemplateUsed(response, 'app/earnings.html')
        self.assertNotIn('answer', response.context)




class TestBoth(SimpleTestCase):
    def test_if_true(self):
        response = self.client.get(
            path=reverse("both"),
            data={
                'input_1': 'True',
                'input_2': 'True'
            },
        )

        self.assertEqual(response.context["answer"], True)

    def test_if_false(self):
        response = self.client.get(
            path=reverse("both"),
            data={
                'input_1': 'False',
                'input_2': 'False'
            },
        )
        self.assertEqual(response.context["answer"], False)

    def test_if_false_or_true(self):
        response = self.client.get(
            path=reverse("both"),
            data={
                'input_1': 'False',
                'input_2': 'True'
            },
        )

        self.assertEqual(response.context["answer"], False)

    def test_if_true_or_false(self):
        response = self.client.get(
            path=reverse("both"),
            data={
                'input_1': 'True',
                'input_2': 'False'
            },
        )
        self.assertEqual(response.context['answer'], False)

# class TestNotTrueNorFalse(SimpleTestCase):
#     def test_empty_check_boxes(self):
#         response = self.client.get(
#             path=reverse("both"),
#             data={
#                 'input_1': '',
#                 'input_2': ''
#             },
#         )
#         self.assertTemplateUsed(response, 'app/both.html')
#         self.assertNotIn('answer', response.context)


class TestWalkOrDrive(SimpleTestCase):
    def test_walk(self):
        response = self.client.get(
            path=reverse('walk_or_drive'),
            data={
                'distance_input': '0.15',
                'is_nice_weather_input': 'True'
            },
        )
        self.assertEqual(response.context['answer'], 'walk')

    def test_drive(self):
        response = self.client.get(
            path=reverse('walk_or_drive'),
            data={
                'distance_input': '1.50',
                'is_nice_weather_input': 'False'
            },
        )
        self.assertEqual(response.context['answer'], 'drive')

    def test_drive_second(self):
        response = self.client.get(
            path=reverse('walk_or_drive'),
            data={
                'distance_input': '5.00',
                'is_nice_weather_input': 'True'
            },
        )
        self.assertEqual(response.context['answer'], 'drive')

class TestInvalidDistance(SimpleTestCase):
    def test_letters_in_distance(self):
        response = self.client.get(
            path=reverse('walk_or_drive'),
            data={
                'distance_input': 'Hello',
                'is_nice_weather_input': 'True'
            },
        )
        
        self.assertTemplateUsed(response, 'app/walk-or-drive.html')
        self.assertNotIn('answer', response.context)


class TestHowPopulated(SimpleTestCase):
    def test_sparsely_populated(self):
        response = self.client.get(
            path = reverse('how_populated'),
            data={
                'population_input': 25000,
                'land_area_input': 285
            },
        )
        self.assertEqual(response.context['answer'], 'Sparsely Populated')

    def test_densely_populated(self):
        response = self.client.get(
            path = reverse('how_populated'),
            data={
                'population_input': 25000,
                'land_area_input': 12
            },
        )
        self.assertEqual(response.context['answer'], 'Densely Populated')

class TestInvalidPopulation(SimpleTestCase):
    def test_letters_in_population(self):
        response = self.client.get(
            path = reverse('how_populated'),
            data={
                'population_input': 'jkdkdl',
                'land_area_input': 12
            },
        )

        self.assertTemplateUsed(response, 'app/how-populated.html')
        self.assertNotIn('answer', response.context)


class TestGoldStars(SimpleTestCase):
    def test_one_star(self):
        response = self.client.get(
            path = reverse('gold_stars'),
            data={
                'score_input': '800',
            }
        )
        self.assertEqual(response.context['answer'], '*')

    def test_two_star(self):
        response = self.client.get(
            path = reverse('gold_stars'),
            data={
                'score_input': '4500',
            }
        )
        self.assertEqual(response.context['answer'], '**')

    def test_three_star(self):
        response = self.client.get(
            path = reverse('gold_stars'),
            data={
                'score_input': '7500',
            }
        )
        self.assertEqual(response.context['answer'], '***')

    def test_four_star(self):
        response = self.client.get(
            path = reverse('gold_stars'),
            data={
                'score_input': '9500',
            }
        )
        self.assertEqual(response.context['answer'], '****')

    def test_five_star(self):
        response = self.client.get(
            path = reverse('gold_stars'),
            data={
                'score_input': '10500',
            }
        )
        self.assertEqual(response.context['answer'], '*****')

class TestInvalidStars(SimpleTestCase):
    def test_empy_stars(self):
        response = self.client.get(
            path = reverse('gold_stars'),
            data={
                'score_input': '',
            }
        )
        
        self.assertTemplateUsed(response, 'app/gold-stars.html')
        self.assertNotIn('answer', response.context)

    
class TestHowManyPoints(SimpleTestCase):
    def test_extra_kick(self):
        response = self.client.get(
            path = reverse('points'),
            data={
                'points_input': 'extra kick'
            }
        )
        self.assertEqual(response.context['answer'], 1)

    def test_extra_conv(self):
        response = self.client.get(
            path = reverse('points'),
            data={
                'points_input': 'extra conv'
            }
        )
        self.assertEqual(response.context['answer'], 2)

    def test_safety(self):
        response = self.client.get(
            path = reverse('points'),
            data={
                'points_input': 'safety'
            }
        )
        self.assertEqual(response.context['answer'], 2)

    def test_feild_goal(self):
        response = self.client.get(
            path = reverse('points'),
            data={
                'points_input': 'fg'
            }
        )
        self.assertEqual(response.context['answer'], 3)

    def test_touchdow(self):
        response = self.client.get(
            path = reverse('points'),
            data={
                'points_input': 'td'
            }
        )
        self.assertEqual(response.context['answer'], 6)

class TestInvalidPoint(SimpleTestCase):
    def test_empty_points(self):
        response = self.client.get(
            path = reverse('points'),
            data={
                'points_input': ''
            }
        )

        self.assertTemplateUsed(response, 'app/points.html')
        self.assertNotIn('answer', response.context)





        

