# SecureScope Architecture


                User
                 |
                 |
              main.py
                 |
                 |
          File Scanner Engine
                 |
        --------------------
        |        |          |
     Readers  Detector   Risk Engine
        |        |          |
        |     Regex +       |
        |     Entropy       |
        |
   TXT CSV PDF DOCX

                 |
                 |
          Report Generator
                 |
                 |
          JSON Export