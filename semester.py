class CourseSorter:
    def __init__(self):
        self.suggested_lessons = {
            1: [("mabani", 3), ("wrk mabani", 1), ("PUB_English", 3), ("math1", 4), ("physic1", 3), ("Pub_pesian", 3), ("wrkshp pub", 1)],
            2: [("java", 3), ("wrk java", 1), ("ghosste", 3), ("math2", 3), ("phycis2", 3), ("expert_eng", 2), ("tafsir_quran", 2), ("tafsirnahj", 2)],
            3: [("data_struc", 3), ("logic_circle", 3), ("defransel", 3), ("physic_az", 1), ("eslamic1", 2), ("elec_circle", 3), ("wrk_lgicircle", 1), ("wrk_elecircle", 1)],
            4: [("statistic", 3), ("1-data base", 3), ("artitect_cumputer", 3), ("liner_jebra", 3), ("eslamic2", 2), ("lang_machine", 3), ("az_artitect_cumputer", 1)],
            5: [("tarbiat_badani", 1), ("culture", 2), ("research", 2), ("operation_sys", 3), ("netwrk_cumptr", 3), ("az_ntwri", 1), ("az_os", 1)],
            6: [("software1", 3), ("internship", 1), ("ayin_zendeghi", 2), ("falsafe", 2), ("akhlagh", 2), ("compiler", 3), ("programing_lang", 3)],
            7: [("varzesh1", 1), ("revelthn_eslamic", 2), ("emam", 2), ("last_prject", 3), ("software2", 3), ("softwaretest", 3), ("ux", 3)],
            8: [("recovery", 3), ("signal", 3), ("accembly", 3), ("optional", 3), ("danesh", 2), ("az_accembly", 1)],
            9: [],
            10: [],
        }

        self.passed_courses = []

    def get_courses(self, semester):
        if semester == 1:
            return self.suggested_lessons[semester]

        if semester > 1:
            previous_semester = semester - 1
            conditional = input(f"Was the previous semester (semester {previous_semester}) conditional? (y/no): ")
            if conditional.lower() == "y":
                max_courses = 14
            else:
                score = float(input("What was your score in the previous semester? "))
                if score >= 16:
                    max_courses = 24
                elif score >= 12:
                    max_courses = 20
                else:
                    max_courses = 0

            max_unit = max_courses - len(self.passed_courses)

            for prev_semester in range(1, semester):
                for course_units in self.suggested_lessons[prev_semester]:
                    course = course_units[0]
                    units = course_units[1]
                    passed = input(f"Did you pass the course '{course}'? (y/no): ")
                    if passed.lower() == "y":
                        self.passed_courses.append(course)
                    else:
                        self.suggested_lessons[semester].append((course, units))

            suggested_courses = self.suggested_lessons[semester]
            remaining_suggested_courses = [(course, units) for course, units in suggested_courses if course not in self.passed_courses]
            print("---------------------------------")
            print(f" you passed this lesson {self.passed_courses}")
            print("---------------------------------------")
            return remaining_suggested_courses[:max_unit] 
            
        


    
        
