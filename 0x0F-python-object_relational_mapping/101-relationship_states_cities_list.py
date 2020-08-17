#!/usr/bin/python3
"""how to use mysql client and compare it so sql alchemy"""
if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, Session, scoped_session
    from sqlalchemy.ext.declarative import declarative_base
    import sys
    from sqlalchemy import Column, String, ForeignKey, Integer
    from relationship_state import Base, State
    from relationship_city import City

    args_ = sys.argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format(
        args_[0], args_[1], 'localhost', args_[2]), pool_pre_ping=True)
    Base.metadata.create_all(engine)  # create like database..

    session_factory = sessionmaker(bind=engine,
                                   expire_on_commit=False)
    Session = scoped_session(session_factory)

    session = Session()

    result = session.query(State).all()

    # print(result)
    for obj_ in result:
        print("{}: {}".format(obj_.id, obj_.name))
        for cities in obj_.cities:
            print("    {}: {}".format(cities.id, cities.name))
