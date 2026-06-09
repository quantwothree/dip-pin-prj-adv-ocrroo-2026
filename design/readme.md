# Overview

Put your design documentation in this folder.
This should include rough notes from the familiarization phase.


## Persona

Write a brief persona of your user using design thinking. You can use the following template:

- **Name**: Kim
- **Age**: 34
- **Occupation**: Junior data analyst
- **Location**: Perth
- **Goals**: To independently consume educational videos content and coding tutorials without needing external assistance.
- **Frustrations**: Kim gets frustrated when an instructor points to a slide or a block of code and says "as you can see here," without verbally describing it. 
- **Motivations**: Career progression, digital autonomy
- **Technology**: Relies on screen reader, uses keyboard-only navigation (no mouse)
- **Experience**: Tech savvy and proficient in navigating complex web applications, provided they have correct ARIA labels and semantic HTML.
- **Personality**: Analytical, determined, independent, and highly organized.
- **Interests**: Machine learning, accessible web design, podcasts, and open-source software advocacy.

Notice: This project focuses on assistive technology for people with disabilities. It is important to treat the topic with respect and sensitivity.

Consider:

- People are not defined by their disabilities.
- People with disabilities are not a homogeneous group.

Your persona should reflect the diversity of people with disabilities and their experiences.

## User Journey

What is the user journey? What are the steps the user takes to achieve their goals?

- **Step 1**: Kim opens the video player and uses the Tab key to navigate to the video player. She uses standard keyboard shortcuts (Spacebar) to begin playing a selected video.

- **Step 2**: The video instructor begins silently typing a block of Python code on the screen. Kim pauses the video using the keyboard, knowing she is missing visual information.

- **Step 3**: Kim presses Tab to reach the  labeled "Extract On-Screen Text" button and presses Enter.

- **Step 4**: The video player returns the OCR text. It then get injected into a dedicated, screen reader accessible text box. Kim's screen reader reads the extracted code aloud, allowing her to copy it to her own notes and resume the video.

## UI Interaction Patterns

What are the UI interaction patterns you will use in your project?

**Keyboard Navigation:** Every interactive element (play, pause, seek, extract text, copy text) is reachable via the Tab, Enter or Space key. No actions will require precise mouse clicks.

**ARIA:** When the user clicks the extraction button, the UI informs the screen reader that the API is "Processing," and then announces when the "Text extraction is complete."

**High Contrast:** For users who have impaired vision but do not rely entirely on screen readers, the currently selected button or text field will feature a high-contrast design so the active state is clearly distinguishable. 

**Semantic HTML:** Using native <button>, <h1>, and <main> tags rather than custom <div> components to ensure maximum compatibility with assistive technologies.

## AI Prompts

Write down any AI prompts you came up with after your first session

- What are the industry best practices for making custom HTML video player controls accessible to screen readers?
- What is ARIA and how to implement them ?
- To implement ARIA into my video player, all I need to do is to add the appropriate HTML tags?
- Would any web apps running on a browser automatically work with keyboard shortcuts?
- Help me understand how screen readers work in general and in a web app