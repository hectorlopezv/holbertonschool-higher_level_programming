#!/usr/bin/python3
"""how to use mysql client and compare it so sql alchemy"""
if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, Session, scoped_session
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String, DateTime
    import sys
    from model_state import Base, State

    args_ = sys.argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format(
        args_[0], args_[1], 'localhost', args_[2]), pool_pre_ping=True)
    Base.metadata.create_all(engine)  # create like database..

    session_factory = sessionmaker(bind=engine,
                                   expire_on_commit=False)
    Session = scoped_session(session_factory)

    session = Session()
    result = session.query(State).filter(State.name.like('%a%'))
    for obj_ in result:
        session.delete(obj_)
    session.commit()
    session.close()
