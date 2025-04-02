from flask import Flask, request, redirect
from pylti1p3.tool_provider import ToolProvider

app = Flask(_name_)

@app.route('/lti-launch', methods=['POST'])
def lti_launch():
    tool = ToolProvider(request.form)

    if tool.is_valid_request():
        user_id = request.form.get('user_id')
        github_redirect_url = f"https://github.com/codespaces/new?user={user_id}"
        return redirect(github_redirect_url)

    return "LTI Authentication Failed", 403

if _name_ == '_main_':
    app.run(host="0.0.0.0", port=5000)
