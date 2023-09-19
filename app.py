from flask import Flask, render_template, send_from_directory, request, redirect
import os

app = Flask(__name__)

#OFFICES_FOLDER = os.path.join(os.getcwd(), "/offices")
OFFICES_FOLDER = os.path.relpath("thishomeofficedoesnotexist/offices")
#OFFICES_FOLDER = os.path.dirname("/offices")

@app.route("/")
def index():
    # Get a list of image filenames in the "offices" folder
    # image_files = os.listdir(OFFICES_FOLDER)
    # return render_template("index.html", image_files=image_files)
    print OFFICES_FOLDER
    return selected_image("abcd")


def selected_image(image_filename):
    image_files = [filename for filename in os.listdir(OFFICES_FOLDER) if filename.lower().endswith('.png')]
    if image_filename == "abcd":
        #image_files = os.listdir(OFFICES_FOLDER)
        return render_template("index.html", image_files=image_files)
    else:
        #image_files = os.listdir(OFFICES_FOLDER)
        return render_template("index.html", image_files=image_files, selected_image=image_filename)


@app.route("/offices/<image_filename>")
def custom_image(image_filename):
    return send_from_directory(OFFICES_FOLDER, image_filename)


@app.route("/<path:image_filename>")
def custom_image_modal(image_filename):
    # Serve the image only if it exists in the "offices" folder
    image_filename = image_filename + ".png"
    image_path = os.path.join(OFFICES_FOLDER, image_filename)

    if os.path.isfile(image_path):
        return selected_image(image_filename)
    else:
        return redirect("/");


if __name__ == "__main__":
    app.run(debug=True)