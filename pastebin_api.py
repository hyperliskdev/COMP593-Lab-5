import requests

API_POST_URL = 'https://pastebin.com/api/api_post.php'
DEV_API_KEY = 'cTmXTeoc098UITN9aUizKYtbzCD7Sl--'


def post_new_paste(title, body, exp='10M', listed=True):
    """Create a new PasteBin paste

    Args:
        title (_type_): paste title
        body (_type_): Main body text of the paste
        exp (str, optional): The enum of future expiry dates (N, 10M, 1H, 1D, 1W, 2W, 1M, 6M, 1Y). Defaults to '10M'.
        listed (bool, optional): Whether this is a public or unlisted paste. Defaults to True.

    Returns:
        str: URL of the new paste.
    """
    # Create the dictionary of request data.
    params = {
        'api_dev_key': DEV_API_KEY,
        'api_option': 'paste',
        'api_paste_code': body,
        'api_paste_name': title,
        'api_paste_expire_date': exp,
        'api_paste_private': 0 if listed else 1
        
    }

    # Send the request
    print("Posting new paste to PasteBin...", end="")
    resp_msg = requests.post(API_POST_URL, data=params)

    # Verify response
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        return resp_msg
    else:
        print('failure')
        print(f'response code: {resp_msg.status_code} ({resp_msg.reason})')
