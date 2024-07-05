import os

# DIR_IMGS = "img/galeria/fotografia"
DIR_IMGS = "img/galeria/community"

result = ""

for dir_img in os.listdir(DIR_IMGS):

    template = f"""
    <div class="grid-item">
        <figure class="effect-ruby">
            <img src="{DIR_IMGS}/{dir_img}" alt="Image" class="img-fluid tm-img">
            <figcaption>
                <a href="{DIR_IMGS}/{dir_img}"></a>
            </figcaption>
        </figure>
    </div>
    """

    result += template

print(result)
