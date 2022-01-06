from .const import CPS

# ----------------------------------------------------------------------
# -------------------- BASE MOVEMENT PARAMS ----------------------------
# ----------------------------------------------------------------------
BASE_ROTATE_SPEED = 20/CPS
BASE_BASE_ROTATE_SPEED = 40/CPS

BASE_MOVE_SPEED_FORWARD = 70/CPS
BASE_MOVE_SPEED_BACK = 50/CPS

# BASE_acceleration
BASE_ACCELERATION = 2/CPS
BASE_ACCELERATION_LOSS = 1/CPS
# ----------------------------------------------------------------------
# -------------------- BASE BULLET PARAMS ------------------------------
# ----------------------------------------------------------------------

BASE_BULLET_MAX_TRACE = 1000

BASE_BULLET_MOVE_SPEED = 250/CPS
BASE_BULLET_SPEED_MOD = 1
BASE_BULLET_SPEED_SLOW = True

# ----------------------------------------------------------------------
# -------------------- BASE FIRE PARAMS --------------------------------
# ----------------------------------------------------------------------

BASE_FIRE_RATE = 5*CPS
BASE_FIRE_DAMAGE = 2