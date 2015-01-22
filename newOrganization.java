
/**
 * Write a description of class newOrganization here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class newOrganization extends Organization implements Record
{
    public newOrganization(String name, String regnum, String type)
    {
       
        super(name,regnum,Organization.OrgType.Public);
        if (type.equals("Private"))
        {
            super.type=Organization.OrgType.Private;
        }
    }
    
    public String getKey()
    {
        return regNum;
    }
}
