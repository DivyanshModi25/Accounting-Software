import enum

from app.db.base import Base
from sqlalchemy import CheckConstraint,String,Enum,ForeignKey,Boolean, Numeric
from sqlalchemy.orm import Mapped,mapped_column,relationship
from typing import Optional,List
from decimal import Decimal



class AccountType(str,enum.Enum):
    ASSET = "ASSET"
    LIABILITY = "LIABILITY"
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
    EQUITY = "EQUITY"


class LedgerGroup(Base):
    __tablename__ = "ledger_groups"

    __table_args__ = (
        CheckConstraint(
            "(is_system = true AND user_id IS NULL) OR (is_system = false AND user_id IS NOT NULL)",
            name="ledger_group_system_user_check"
        ),
    )


    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(150),nullable=False)

    account_type:Mapped[AccountType] = mapped_column(
        Enum(AccountType,name="account_type_enum"),
        nullable=False
    )

    parent_id:Mapped[Optional[int]] = mapped_column(
        ForeignKey("ledger_groups.id",ondelete="CASCADE"),
        nullable=True
    )

    user_id:Mapped[int] = mapped_column(
        ForeignKey("Users.id",ondelete="CASCADE"),
        nullable=True 
    )


    is_system:Mapped[bool] = mapped_column(Boolean,default=False)
    is_active:Mapped[bool] = mapped_column(Boolean,default=True)


    #Relationships

    parent:Mapped[Optional["LedgerGroup"]] = relationship(
        "LedgerGroup",
        remote_side="LedgerGroup.id",
        back_populates="children"
    )

    children:Mapped[List["LedgerGroup"]] = relationship(
        "LedgerGroup",
        back_populates="parent",
        cascade="all, delete"
    )


    ledgers:Mapped[List["Ledger"]] = relationship(
        "Ledger",
        back_populates="group",
        cascade="all, delete"
    )



class BalanceType(str,enum.Enum):
    DEBIT="DEBIT"
    CREDIT="CREDIT"



class Ledger(Base):
    __tablename__="ledgers"

    __table_args__ = (
    CheckConstraint(
        "(is_system = true AND user_id IS NULL) OR (is_system = false AND user_id IS NOT NULL)",
        name="ledger_system_user_check"
    ),
)

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(150),nullable=False)

    group_id:Mapped[int] = mapped_column(
        ForeignKey("ledger_groups.id",ondelete="CASCADE"),
        nullable=False
    )

    user_id:Mapped[int] = mapped_column(
        ForeignKey("Users.id",ondelete="CASCADE"),
        nullable=True
    )

    opening_balance:Mapped[Decimal] = mapped_column(
        Numeric(18,2),
        default=Decimal("0.00")
    )

    opening_balance_type:Mapped[BalanceType] = mapped_column(
        Enum(BalanceType,name="balance_type_enum"),
        default=BalanceType.DEBIT
    )

    is_system: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)


    #Relationships
    group:Mapped[LedgerGroup] = relationship(back_populates="ledgers")