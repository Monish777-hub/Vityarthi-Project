# AlgoLabs Architecture

```text
                    +----------------+
                    |    main.py     |
                    |  CLI / Menus   |
                    +-------+--------+
                            |
             +--------------+--------------+
             |              |              |
             v              v              v
      algorithms.py   array_tools.py   search_sort.py
             |              |              |
             +--------------+--------------+
                            |
                            v
                       quiz.py
                            |
                            v
                    data/questions.json
```

The application follows a simple modular architecture. The main module handles navigation and user interaction, while algorithm modules contain reusable functions. The quiz module loads questions from JSON data.
