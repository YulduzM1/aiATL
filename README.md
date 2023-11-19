# aiATL
# Essay Insight Generator
## Overview
This application leverages Vertex AI and the Text Generation Model to provide teachers with valuable insights into their students' essays. By segmenting each essay into discrete rhetorical and argumentative elements, the system classifies these elements and offers feedback on areas that require improvement.
## Getting Started
Follow the steps below to set up and run the application:

Install the required dependencies:
   ```bash
   pip install vertexai
   ```

Clone the repository:
   ```bash
   git clone https://github.com/your-username/essay-insight-generator.git
   cd essay-insight-generator
   ```

Initialize Vertex AI with your project and location:
   ```python
   import vertexai
   vertexai.init(project="your-project-id", location="your-location")
   ```

Customize the parameters based on your preferences:
   ```python
   parameters = {
       "candidate_count": 1,
       "max_output_tokens": 1024,
       "temperature": 0.2,
       "top_p": 0.8,
       "top_k": 40
   }
   ```

Load the Text Generation Model:
   ```python
   from vertexai.language_models import TextGenerationModel
   model = TextGenerationModel.from_pretrained("text-bison")
   ```

Make predictions on essays and obtain valuable insights:
   ```python
   response = model.predict("""
   You are a grader for grade 6-12 students who are writing essays.
   You will first need to segment each essay into discrete rhetorical
   and argumentative elements (i.e., discourse elements) and then
   classify each element as one of the following and most importantly,
   give feedback on what the essay is missing or does poorly.
   """)
   ```

Analyze the `response` to provide feedback to teachers and students.
## Contributing
We welcome contributions! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.
## License
This project is licensed under the [MIT License](LICENSE).














