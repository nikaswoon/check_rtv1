PATH_RTV1 = "/Users/dtaisha/rtv1_git_hub/rtv1"
PATH_SCENE = "/Users/dtaisha/rtv1_git_hub/scenes/scene_4"
TEST_DATA_DOUBLES = {"1.1": 1.10,
                     "1.": 1.00,
                     "1": 1.00,
                     "0": 0.00,
                     "-1": -1.00,
                     "-1.95": -1.95,
                     "-1.05": -1.05,
                     "1.95": 1.95,
                     "1.05": 1.05,
                     "-0": 0.00,
                     "-0.05": -0.05,
                     "-0.005": 0.00,
                     "0.0914523547687654321234567": 0.09,
                     "2147483647": 2147483647.00,
                     # "2147483648": 2147483648.00,
                     # "2147483648.": 2147483648.00,
                     # "2147483648.2147483648": 2147483648.21,
                     "-2147483648.": -2147483648.00,
                     "-.": 0.00,
                     "-.13456": -0.13,
                     "-.wert": 0.00,
                     ".2ert": 0.20,
                     "134eqr.2ert": 134.20,
                     "eqr.q3rt": 0.03,
                     }
TEST_NOT_FULL_SPHERE = [
    "sphere\t-10.9 0.0 4.0\t0.1\tred\t30\n", "sphere\t-10.9 0.0 4.0\t0.1\tred\t\n", "sphere\t-10.9 0.0 4.0\t0.1\n",
    "sphere\t-10.9 0.0 4.0\n", "sphere\t-10.9\n"]
TEST_NOT_FULL_CYLINDER = [
    "cylinder\t1.0 0.0 10.1\t1.2\tyellow\t1.0 1.0 0.0\t67\n",
    "cylinder\t1.0 0.0 10.1\t1.2\tyellow\t1.0 1.0 0.0\n",
    "cylinder\t1.0 0.0 10.1\t1.2\tyellow\n",
    "cylinder\t1.0 0.0 10.1\t1.2\n",
    "cylinder\t1.0 0.0 10.1\n",
    "cylinder\t1.0 0.0\n",
]
TEST_NOT_FULL_CONE = [
    "cone\t3.0 0.0 50.0\tmetal\t1.0 0.0 0.0\t20\t90\n",
    "cone\t3.0 0.0 50.0\tmetal\t1.0 0.0 0.0\t20\n",
    "cone\t3.0 0.0 50.0\tmetal\n",
    "cone\t3.0 0.0 50.0\t\n",
    "cone\t3.0 0.0\n"]
TEST_NOT_FULL_PLANE = [
    "plane\t6.0 0.0 100.0\tpink\t0.0 0.0 1.0\t10\n",
    "plane\t6.0 0.0 100.0\tpink\t0.0 0.0 1.0\t\n",
    "plane\t6.0 0.0 100.0\tpink\t\n",
    "plane\t6.0 0.0 100.0\n",
    "plane\t6.0 0\n"]
TEST_NOT_FULL_CAMERA = [
    "camera\t0.0 0.0 0.0\t0.0 1.0 0.0\n",
    "camera\t0.0 0.0 0.0\n"]

TEST_NOT_FULL_LIGHT = [
    "light\tAMBIENT\t0.9\n",
    "light\tAMBIENT\n",
    "light\tPOINT\t0.8\t5.0 0.0 -2.0\tred\n",
    "light\tPOINT\t0.8\t5.0 0.0 -2.0\n",
    "light\tPOINT\t0.8\n",
    "light\tPOINT\n"]
