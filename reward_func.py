import math

DIRECTION_THRESHOLD = 10.0

class Reward:

    def __init__(self):
        # used to record history action
        self.steering_angles = []

    def reward_function(self, params):

        # just stop
        if not params['all_wheels_on_track']:
            return 1e-3

        # speed
        speed_reward = params['speed'] 

        # Read input variables
        waypoints = params['waypoints']
        closest_waypoints = params['closest_waypoints']
        heading = params['heading']

        # Align direction
        align_reward = 2.0
        next_point = waypoints[closest_waypoints[1]]
        prev_point = waypoints[closest_waypoints[0]]
        track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
        track_direction = math.degrees(track_direction)
        direction_diff = abs(track_direction - heading)
        if direction_diff > 180:
            direction_diff = 360 - direction_diff
        if direction_diff > DIRECTION_THRESHOLD:
            align_reward *= 0.3

        # curvature vs speed
        if abs(params["steering_angle"]) > 15 and params["speed"] > 2:
            speed_reward *= 0.1

        # track following
        follow_reward = 0.1
        track_width = params['track_width']
        distance_from_center = abs(params['distance_from_center'])
        if  distance_from_center < 0.3 * track_width:
            follow_reward = 2.0

        # Smooth driving
        smooth_reward = 3.0
        self.steering_angles.append(params["steering_angle"])
        if len(self.steering_angles) > 1:
            if abs(self.steering_angles[-2] - self.steering_angles[-1]) > DIRECTION_THRESHOLD:
                smooth_reward *= 0.1

        # Make sure complete laps
        progress_reward = 1.0
        if (params['steps'] % 5) == 4:
            progress_reward += 1

        reward =  ( speed_reward + align_reward + smooth_reward + follow_reward ) * progress_reward
        if reward <= 0.0:
            reward = 1e-3

        return reward

reward_object = Reward()
def reward_function(params):
    return reward_object.reward_function(params)
