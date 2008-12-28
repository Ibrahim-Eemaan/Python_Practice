applicants_dict = {
    'Anna' : {'experience': 2, 
            'languages' : ['Python', 'Ruby', 'Rust', 'Java'],
            'proj_supervision': False },
    
    'Ben' : {'experience': 5, 
            'languages' : ['Java', 'Haskell', 'C++', 'Perl'],
            'proj_supervision': False },
    
    'Calvin' : {'experience': 3, 
            'languages' : ['C', 'Python', 'Java', 'Scala'],
            'proj_supervision': True },
            
    'Dorothy' : {'experience': 6, 
            'languages' : ['Java', 'Python', 'Elm', 'Clojure'],
            'proj_supervision': False },

    'Esther' : {'experience': 4, 
            'languages' : ['Java', 'Go', 'Ruby', 'C#'],
            'proj_supervision': True }    
}

min_experience = 4
required_languages = ['Python', 'Java']
for name, cv_dict in applicants_dict.items():
    if cv_dict['experience'] >= min_experience and (set(required_languages).issubset(cv_dict['languages']) or cv_dict['proj_supervision']):
        print(f'{name}  passes the screening')