physical = ['Marketing',
            'Designer',
            'Researcher',
            'Research',
            'Technician',
            'Cosmetologist',
            'Accountant',
            'Customer Service',
            'Call Center',
            'Scientist',
            'Actuary',
            'Architect',
            'Public Relations',
            'Assistant',
            'Bank',
            'Manager',
            'Drafter',
            'Archivist',
            'Attorney',
            'Paralegal',
            'HR',
            'Human Resources',
            'Recruiter',
            'Receptionist',
            'Secretary',
            'Clerk',
            'Pharmacist',
            'Medical',
            'Data',
            'Analyst',
            'Engineer',
            'Computer',
            'Developer',
            'DevOps',
            'Chemist',
            'Sociologist',
            'Mathematician',
            'Physicist',
            'Mentor',
            'Teacher',
            'Tutor',
            'Artist',
            'Editor',
            'Animator',
            'Musician',
            'Writer',
            'Anchor',
            'Counselor',
            'Entrepreneur']

learning = ['Mentor',
            'Teacher'
            'Teaching',
            'Assistant',
            'Substitute',
            'Daycare',
            'Counselor',
            'Graphic',
            'Designer',
            'Producer',
            'Musician',
            'Writer',
            'Animator',
            'Actor',
            'Sound',
            'Beautician',
            'Hair',
            'Journalist',
            'Editor',
            'Manager,'
            'Receptionist',
            'Secretary',
            'Cashier',
            'Worker',
            'Retail',
            'Construction',
            'Warehouse',
            'Nurse',
            'Practitioner',
            'Doctor',
            'Caregiver',
            'CNA',
            'Physical Therapist',
            'Therapist',
            'Sales',
            'Associate',
            'Waiter',
            'Waitress',
            'Server',
            'Chef',
            'Barista',
            'Cook',
            'Computer',
            'Scientist',
            'IT',
            'UX',
            'Developer',
            'Devops',
            'SQL',
            'Web',
            'Software',
            'Data',
            'Programmer',
            'Network',
            'Personal',
            'Real Estate',
            'Planner',
            'Entrepreneur',
            'Public Relations',
            'Call Center',
            'Teller',
            'Recruiter',
            'Plumber',
            'Housekeeper',
            'Flight Attendant',
            'News',
            'Anchor',
            'Courier']

mental = ['Analyst',
          'Data',
          'Financial',
          'Engineer',
          'Mechanical',
          'Civil',
          'Electrical',
          'Computer',
          'Scientist',
          'IT',
          'UX',
          'Developer',
          'Devops',
          'SQL',
          'Web',
          'Software',
          'Data',
          'Programmer',
          'Network',
          'DevOps',
          'Cosmetologist',
          'Research',
          'Researcher',
          'Accountant',
          'Bookkeeper',
          'Dental',
          'Physical Therapy',
          'Graphic',
          'Designer',
          'Producer',
          'Musician',
          'Writer',
          'Animator',
          'Actor',
          'Sound',
          'Video',
          'Editor',
          'Welder',
          'Plumber',
          'Massage',
          'Entrepreneur',
          'Worker',
          'Math',
          'Carpenter',
          'Taper']


def match(name, type_job):
    if any(x in type_job for x in name):
        return True
    else:
        return False
