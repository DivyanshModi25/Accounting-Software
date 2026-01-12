from sqlalchemy.orm import Session


from app.db.models.ledger_models import LedgerGroup


def get_group_tree(db:Session,user_id:int):
    
    groups = db.query(LedgerGroup).filter(
        (LedgerGroup.is_active) & ((LedgerGroup.user_id==user_id) | (LedgerGroup.is_system))
    ).all()

    group_map = {g.id:g for g in groups}

    children_map={}

    for g in groups:
        children_map.setdefault(g.parent_id,[]).append(g)


    def build(group):
        return {
            "id":group.id,
            "name":group.name,
            "account_type":group.account_type,
            "children":[build(child) for child in children_map.get(group.id,[])],
            "ledgers":group.ledgers
        }
    
    roots = [g for g in groups if g.parent_id is None]
    return [build(g) for g in roots]