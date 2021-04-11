<h1 align="center">Welcome to dystic-api</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/arnavs-0/dystic-api/blob/main/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

![Image of Logo](https://media.discordapp.net/attachments/746184734111039670/746726388719026237/dystic.png)
![Image of Slogan](https://media.discordapp.net/attachments/746184734111039670/746726390623371414/making_job_search_more_accessible..png)


> An Indeed Scraper to Find Jobs that suit a certain keywords given a condition. Please note that this scraper
> is used for educational purposes. Please use at your own risk. See License for more details.

### 🏠 [Homepage](https://github.com/arnavs-0/dystic-api)

### ✨ [Project Home](https://dystic.web.app/)

### [Learn More about our Project](https://devpost.com/software/dystic)

## Install

```sh
pip install -r requirements.txt
```

## Usage

```sh
python app.py
```

Example URL Request:

```
http://127.0.0.1:5000/jobs?jt=software&jl=california&jn=learning
```
There are 3 Parameters taken, 
```jt``` which takes in a job keyword,
```jl``` which is a location (So far US Cities and States are supported) and
```jn``` parameter which is able to filter jobs based on conditions (we are hoping to make this parameter optional in the near future)

**Note**

If you receive an empty response that generally means there is a captcha blocking the request. As a workaround go to Indeed's website and finish the captcha challenge

## Future Plans

* We hope to support an international search so users outside the US are able to use it

* Find a workaround for the Indeed captcha

* Implement ML to return jobs suitable for any user rather than using only keywords

* and more!

## Authors

👤 **arnavs-0, andytubeee, Sohil1926, staranger01**

* Github: 
  
[@arnavs-0](https://github.com/arnavs-0)
  
[@andytubeee](https://github.com/andytubeee)

[@Sohil1926](https://github.com/Sohil1926)

[@staranger01](https://github.com/staranger01)
 

## 🤝 Contributing

Contributions, issues and feature requests are welcome!
<br />Feel free to check [issues page](https://github.com/arnavs-0/dystic-api/issues). 

Contributing Guidelines Here:

## Show your support

Give a ⭐️ if this project helped you!


## License

```
Copyright (c) 2021 arnavs-0, andytubeee, Sohil1926, staranger01

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
