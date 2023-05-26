This is my first nix package that builds an environment which includes the required packages `requests` and `bs4` and after using `nix-shell` it starts the environment in which it includes the packages in environment and then running the `main.py`.

I have included python3 and Git to my global environment by configuring the home.nix file and others packages are included in project directories only.

This python code requests the wikipedia and scrape the text provided using `beautifulsoup4`.

Also i have created a Default.nix file for my personal portofolio website and included nodejs and yarn in environment and started the react script in nix-shell, [here's the link](https://github.com/amrht/amrht.github.io) .
