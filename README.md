# Facebook Photo and Video Downloader

Uses Python's `webbrowser` module to open photos. Automates the saving of those photos by controlling the mouse and keyboard with `pydirectinput`.

#### Motivation

I had a friend whose account was hacked and then the email and phone number were changed so they were locked out. Facebook support was being slow. I'm still friends with them, so I was able to log in to Facebook and open/save all their photos programmatically.

#### /photos_of, /photos_by

1. Visit the photos page and scroll to the bottom to load all links.
2. Inspect Element and copy the `<html>` to `photos.html` in this directory. This file is read by `main.py`.
3. `python main.py`. This is configured to open photos one at a time in Chrome on Windows (change the code to whatever browser you need). You may also consider slicing the list of photos to just the first few as you try it out.

> Sometimes, the mouse movements hover over a tagged portion of the image. When that happens, the image is not saved but the tab remains open. You'll have to go back and save it yourself. I ran the code for about 1000 images that this was only a problem for about a dozen of them.

#### /videos

Use https://fdown.net/index.php or similar to download if the video is public.
If the video is private, then the best way I could find is this:

1. Visit the video page.
2. Inspect Element and copy the `<html>` to a file.
3. Search the file for the `<video>` tag (there is only one) and extract the `src`.
4. Replace all `&amp;` with `&`. (see [https://stackoverflow.com/a/64731507/18274577](https://stackoverflow.com/a/64731507/18274577))
5. Open the URL in a browser and you're good to go.
