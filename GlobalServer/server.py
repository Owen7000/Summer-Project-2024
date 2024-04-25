import datetime

from flask import Flask


app = Flask(__name__)

# Global Variables
kill_switch_is_activated : bool = False # If true, no Kiosks can make sales
kill_switch_activation_reason : str = "" # There must be a reason supplied for the kill switch to be activated
kill_switch_end : datetime.datetime = datetime.datetime.now() # The end time of the Kill Switch
kill_switch_has_end_time : bool = True # Is there an expected end time for the Kill Switch?


# Safety Systems Section

@app.route('/safety/ks') # Safety Systems - Kill Switch
def kill_switch_check():
    """Returns the state of the kill switch which controls all kiosk systems"""
    return {
        "kill_switch_is_activated" : kill_switch_is_activated,
        "kill_switch_activation_reason" : kill_switch_activation_reason,
        "kill_switch_end" : kill_switch_end,
        "kill_switch_has_end_time" : kill_switch_has_end_time
    }


if __name__ == "__main__":
    app.run()