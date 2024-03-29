
pipeline {
    agent any
    stages {
        stage("Running Application") {
            steps {
                script { 
                    echo "Startig Running Application"
                    sh 'python3 file.py'
                }
            }
        }
        stage("Second Stage") {
            steps {
                script { 
                    echo "****************** Hello  **************"
                }
            }
        }
    }
}