from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client["homeoffice"]
users = db["users"]
timeRecording = db["timeRecording"]


def get_user(username, password):
    """Gibt einen Benutzer zurueck
    :param username: Benutzername
    :param password: Passwort
    :return: Benutzer
    """
    return users.find_one({'username': username, 'password': password})


def start(start_day, start_time):
    """Fuegt die Startzeiten ein
    :param start_day: Aktueller Tag
    :param start_time: Start-Uhrzeit
    :return: True, wenn erfolgreich, sonst False
    """

    result = timeRecording.insert_one(
        {
            "day": start_day,
            "start": start_time,
            "stop": ""
        }
    )

    if result.inserted_id:
        return True

    return False


def stop(start_day, start_time, stop_time):
    """Aktualisiert die Uhrzeit, fügt das Beenden der Arbeitszeit ein
    :param start_day: Aktueller Tag
    :param start_time: Start-Uhrzeit
    :param stop_time: Stop-Uhrzeit
    :return: True, wenn erfolgreich, sonst False
    """

    result = timeRecording.update_one(
        {
            "day": start_day,
            "start": start_time
        },
        {
            "$set": {"stop": stop_time}
        }
    )

    return result.matched_count > 0


def get_rec_data(date):
    """Gibt die Urzeit für einen bestimmten Tag zurueck
    :param date: Tag, für den die Uhrzeit zurueckgegeben werden soll
    :return:
    """

    return timeRecording.find({"day": date})
