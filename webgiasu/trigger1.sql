--market
create or replace function deletepostmarket()
returns trigger as
$$
        begin
                delete from market_marketpost where market_marketpost.author_id = OLD.id;
				return NEW;
        end;
$$ language plpgsql;

create trigger deletepostmarket
after delete on profiles_user
FOR EACH ROW EXECUTE FUNCTION deletepostmarket();

--tutor
create or replace function deleteposttutor()
returns trigger as
$$
        begin
                delete from tutor_findtutorpost where tutor_findtutorpost.author_id = OLD.id;
				return NEW;
        end;
$$ language plpgsql;

create trigger deleteposttutor
after delete on profiles_user
FOR EACH ROW EXECUTE FUNCTION deleteposttutor();

--Employee
create or replace function deletepostemployee()
returns trigger as
$$
        begin
                delete from employee_employeepost where employee_employeepost.author_id = OLD.id;
				return NEW;
        end;
$$ language plpgsql;

create trigger deletepostemployee
after delete on profiles_user
FOR EACH ROW EXECUTE FUNCTION deletepostemployee();