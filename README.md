<h2 align="center">Video Chat</h2>

1. ⚙️ [Tech Stack](#tech-stack)
2. 🤸 [Quick Start](#quick-start)
3. 🕸️ [Code Snippets](#snippets)
4. 🚀 [More](#more)

## <a name="tech-stack">⚙️ Tech Stack</a>

- Django
- HTML5
- CSS
- GegoCloud
- Python

## <a name="quick-start">🤸 Quick Start</a>

Follow these steps to set up the project locally on your machine.

**Create virtual environment**

```bash
pip install virtualenv
virtualenv myenv
```

Replace `myenv` with the desired name for your virtual environment.

**Activate the virtual environment**

- Windows

```bash
myenv\Scripts\activate
```

- macOS/Linux

```bash
source myenv/bin/activate
```

**Install Django**

```bash
pip install django
```

**Project Setup**

```bash
django-admin startproject myproject
cd myproject
```

**Cloning the Repository**

```bash
git clone https://github.com/SubhamSaha9/video-chat.git .
```

Replace the values with your actual [GegoCloud](https://www.googleadservices.com) credentials.

**Running the Project**

```bash
python manage.py runserver
```

## <a name="snippets">🕸️ Code Snippets</a>

<details>
<summary><code>style.css</code></summary>

```css
/* Import Google font - Poppins */
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

:root {
  --yellow: #f5c32c;
  --orange: #fca61f;
  --black: #242d49;
  --gray: rgba(36, 45, 73, 0.65);
  --profileShadow: 0px 4px 17px 2px rgba(0, 0, 0, 0.25);
  --hrColor: #cfcdcd;
  --cardColor: rgba(255, 255, 255, 0.64);
  --buttonBg: linear-gradient(98.63deg, #f9a225 0%, #f95f35 100%);
  --buttonBgHover: linear-gradient(98.63deg, #d98919 0%, #d13205 100%);
  --inputColor: rgba(40, 52, 62, 0.07);
  --photo: #4cb256;
  --video: #4a4eb7;
  --location: #ef5757;
  --schedule: #e1ae4a;
}

body {
  overflow: hidden;
  color: #242d49;
  background-color: #f3f3f3;
  padding: 1rem 1rem;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.intro {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
}

.intro-left img {
  height: 30rem;
}

.intro-right {
  height: auto;
  width: 50%;
  display: flex;
  flex-direction: column;
}
.intro-right > h1 {
  font-size: 2.3rem;
  background-color: red;
  background-image: var(--buttonBg);
  background-size: 100%;
  background-repeat: repeat;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-background-clip: text;
  -moz-text-fill-color: transparent;
}

.intro-right a {
  width: 50%;
  margin: 1rem 0;
  background-image: var(--buttonBg);
  padding: 5px 10px;
  font-size: 20px;
  text-decoration: none;
  color: white;
  text-align: center;
  border-radius: 5px;
}

.container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  max-width: 430px;
  width: 100%;
  background: #fff;
  border-radius: 7px;
  box-shadow: 0 5px 10px rgba(246, 76, 76, 0.464);
}

.container .form {
  padding: 2rem;
}

.form header {
  font-size: 2rem;
  font-weight: 500;
  text-align: center;
  margin-bottom: 1.5rem;
}

.form input {
  height: 60px;
  width: 100%;
  padding: 0 15px;
  font-size: 17px;
  margin-bottom: 1.3rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  outline: none;
}

.form input:focus {
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.2);
}

.form input.button {
  color: #fff;
  background-image: var(--buttonBg);
  font-size: 1.2rem;
  font-weight: 500;
  letter-spacing: 1px;
  margin-top: 1.7rem;
  cursor: pointer;
  transition: all 0.4s ease-in-out;
}

.form input.button:hover {
  background-image: var(--buttonBgHover);
}

/* center the div named dashboard */
.dashboard {
  width: 60%;
  height: 50%;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #242d49;
  background-color: #f3f3f3;
  border: 2px solid #f94b1a58;
  border-radius: 7px;
  box-shadow: 0 5px 10px rgba(246, 76, 76, 0.464);
}

/** align the text inside the div named dashboard to the center */
.dashboard h1 {
  font-size: 50px;
  font-weight: bold;
  text-align: center;
  color: black;
}

.dashboard h1 > span {
  background-color: red;
  background-image: var(--buttonBg);
  background-size: 100%;
  background-repeat: repeat;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-background-clip: text;
  -moz-text-fill-color: transparent;
}

.dashboard a {
  background-image: var(--buttonBg);
  border: none;
  border-radius: 7px;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  color: white;
}

.dashboard a {
  margin-top: 7px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}

.dashboard a:hover {
  background-image: var(--buttonBgHover);
}

.dashboard {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

</details>

<details>
<summary><code>auth/style.css</code></summary>

```css
/* Import Google font - Poppins */
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

:root {
  --yellow: #f5c32c;
  --orange: #fca61f;
  --black: #242d49;
  --gray: rgba(36, 45, 73, 0.65);
  --profileShadow: 0px 4px 17px 2px rgba(0, 0, 0, 0.25);
  --hrColor: #cfcdcd;
  --cardColor: rgba(255, 255, 255, 0.64);
  --buttonBg: linear-gradient(98.63deg, #f9a225 0%, #f95f35 100%);
  --inputColor: rgba(40, 52, 62, 0.07);
  --photo: #4cb256;
  --video: #4a4eb7;
  --location: #ef5757;
  --schedule: #e1ae4a;
}

body {
  overflow: hidden;
  color: #242d49;
  background-color: #f3f3f3;
  padding: 1rem 1rem;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.blur {
  position: absolute;
  width: 22rem;
  height: 14rem;
  border-radius: 50%;
  background-color: #a6ddf0;
  filter: blur(72px);
}

#blur-1 {
  top: -18%;
  right: 0;
}
#blur-2 {
  top: 36%;
  left: -8rem;
}

.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 50%;
  width: 65%;
}

.auth {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  gap: 4rem;
  position: relative;
}

.auth > div {
  display: flex;
  align-items: center;
  justify-content: center;
}

.a-left {
  gap: 2rem;
}

.a-left > img {
  width: 4rem;
  height: 4rem;
}

.webName > h1 {
  font-size: 3rem;
  background-color: red;
  background-image: var(--buttonBg);
  background-size: 100%;
  background-repeat: repeat;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-background-clip: text;
  -moz-text-fill-color: transparent;
}

.webName > h6 {
  font-size: 0.85rem;
}

.form-box {
  min-height: 300px;
  min-width: 280px;
  max-width: 370px;
  background-color: #f7ededd7;
  border-radius: 10px;
  padding: 20px;
  box-shadow: #f08b6d 5px 5px 15px;
}

.form-box > header {
  font-weight: 700;
  font-size: 30px;
  text-align: center;
  margin-top: 20px;
  margin-bottom: 10px;
}

.form {
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: space-around;
  height: 80%;
}

.form div {
  width: 100%;
}

.input-name {
  display: flex;
  gap: 1.5rem;
}
.input-name div {
  width: 175px;
}
.form div input {
  width: 100%;
  border: none;
  border-bottom: 2px solid #f7886a;
  height: 30px;
  border-radius: 5px;
  padding: 7px 5px;
  margin-top: 3px;
  margin-bottom: 7px;
}

.button {
  background-image: var(--buttonBg);
  padding: 4px 12px;
  border: none;
  border-radius: 3px;
  font-size: 15px;
  margin-top: 10px;
  color: white;
}
```

</details>

## <a name="more">🚀 More</a>

For more such projects visit my [Github](https://github.com/SubhamSaha9) page.
